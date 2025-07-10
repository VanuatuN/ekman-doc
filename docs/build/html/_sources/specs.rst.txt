Ekman Cluster Specifications
============================

Knowing the specs of the cluster is important, as it allows you to carefully balance your computation and to choose 
the right partition (or "queue") for the calculation you have to perform.

Specs Sheet
-----------

* Name: **Ekman**
* Operating System: = 3.10.0-1160.el7.x86_64 GNU/Linux 
* Scheduler: **SLURM 19.05.3**
* Nodes:

  * **1 x Login Node** (:code:`sail.msk.ru -p 2240`) configured as:

    * Model: ASUS RS700-E10-RS4U
    * CPU: 
      * 56 x Intel(R) Xeon(R) Gold 6348 CPU @ 2.60GHz, 28 cores per socket × 2 sockets 
      *  Total: 112 logical CPUs (threads) as Hyper-Threading is enbaled on the login node.

    * RAM: 256 GiB
    * Swap: 8 GiB
    * Disk: 2 × 894 GiB SSDs in RAID1

      * ~100 GiB for `/home` 

      * ~789 GiB for root `/` 

  * **34 x Compute Nodes** in total: see the Partition section.

  * **1 x GPU node**:

    * CPU: 176 x Intel(R) Xeon(R) Gold 6348 CPU @ 2.60GHz
      * Each node has 2 sockets × 44 cores × 2 threads per core (Hyper-Threading enabled), totaling 176 logical CPUs.

    * GPU:
      * 2 × NVIDIA H100 (14592 CUDA cores each, 80 GiB HBM2e memory per card)
      * Total: 29184 CUDA cores

* Disk:
  
  * Filesystem: Lustre

* Storage

    * :code:`/storage/ekman` Large-volume storage based on SAS drives. This is the default storage for general-purpose data and compute tasks.

    * :code:`/storage/scratch` Fast SSD-based storage intended for temporary high-performance tasks. Files older than 3 months are automatically deleted. Recommended for jobs running on the rack1 partition to benefit from local high-speed interconnects.

    * :code:`/storage/kubrick`, :code:`/storage/tartar`, :code:`/storage/thalassa` Network file systems (NFS). These storages are not suitable for direct compute jobs, but they are available for storing or accessing large datasets.

    * :code:`!!! Storage Policy !!!`

    * Each user is automatically provided with a dedicated directory under every listed storage path (e.g. /storage/ekman/username, /storage/scratch/username, etc.). All work must be done inside your personal directory within these storage locations.

    * **(!!!)** Do not run jobs or store data in your $HOME directory — it is not designed for :code:`I/O-heavy` operations or scratch data.


..   * :code:`/home`:

..     * Total: ?? TiB (2 x OST with ?? TiB each)

..     * User quota: **?? GiB (hard limit: ?? GiB)**

..   * :code:`/scratch`:

..     * Total: ?? TiB (2 x OST with ?? TiB each)

..     * User quota: **?? GiB (hard limit: ?? GiB)**



Partitions
----------

The partitions (queues) are then organized as follows; note that you can get detailed information about a partition via the command :code:`scontrol show Partition=<name>`.

.. table:: Max resources you can ask for each partition. (*): max ?? nodes. (**): max ?? nodes.
   :align: center
   :widths: auto

  +-------------+---------+--------------+-----------------+---------------+------------+
  | Partition   | | Max   | | Max Time   | | Max Memory    | | Max Threads | | Max GPUs |
  |             | | Nodes | | (HH:MM:SS) | | per Node (MB) | | per Node    | | per Node |
  +=============+=========+==============+=================+===============+============+
  | rack1       |    11   | 30-00:00     | ???             |       ??      |     \-     |
  |             |         |              |                 |               |            |
  |             |         |              | ??????          |               |            |
  |             |         |              |                 |               |            |
  |             |         |              | ??????????      |               |            |
  +-------------+---------+--------------+-----------------+---------------+------------+
  | broadwellr2 |    ?    | 30-00:00     | ?????           |       40      |     \-     |
  |             |         |              |                 |               |            |
  |             |         |              | ??????          |               |            |
  |             |         |              |                 |               |            |
  |             |         |              | ??????          |               |            |
  +-------------+---------+--------------+-----------------+---------------+------------+
  | r2c2        |   ?     | 30-00:00     | ?               |       ?       |     \-     |
  |             |         |              |                 |               |            |
  +-------------+---------+--------------+-----------------+---------------+------------+
  | knl         |   ?     | 30-00:00     | ?               |       ?       |     \-     |
  |             |         |              |                 |               |            |
  +-------------+---------+--------------+-----------------+---------------+------------+
  | gpu         |         | ?            | ???????         |       ??      |      2     |
  +-------------+---------+--------------+-----------------+---------------+------------+


.. .. .. note:: **Clarification on max memory:** on the the broadwellr2, r2c2 and rack1 queues you can normally ask for ??? MB max memory. However, there are also additional nodes with bigger memory. As as you can see in the :ref:`Specs Sheet<Specs Sheet>`, though, there are not enough "big memory" nodes for all the possible configurations, as there are only ?? nodes with ?? MB max memory and only ?? nodes with ?? MB max memory. This means you have to be careful with big memory nodes if you queue jobs in ?? or ??. For example, it makes little sense to queue a job requiring all the ?? nodes with ?? MB max memory in the wide queue, which in principle is useful only for a number of nodes greater than ??. Since there are only ?? nodes with ?? MB max memory, it would make more sense to take advantage of the increased max time in the ? queue and queue it there.

.. .. .. note:: **Clarification on threads:** since Hyper-Threading is enabled on all nodes, there are 2 threads per physical core. However, in SLURM's job script language, every thread is a CPU; this means that if you ask for "40 CPUs" in regular1 you are actually asking 40 threads, which is 20 physical cores. For a clarification on the definition on socket, core and thread take a look at the picture below.

.. figure:: res/mc_support.png
   :width: 67%
   :alt: ulysses
   :align: center
   
   Definitions of Socket, Core, & Thread. From `SLURM's documentation <https://slurm.schedmd.com/mc_support.html>`_.



