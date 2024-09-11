Ekman's Specs Sheet
==============


Ekman was launched in exteneded new architecture in September 2024.

This new infrastructure consists of additional nodes and an upgraded software stack.
Ekman works under a job scheduler, **SLURM** (Simple Linux Utility for Resource Management). 
The old nodes are used in partitions **???**, **???**, while the new nodes are available as **broadwellr2**, **r2c2**, **rack1**, **knl** and **gpu**.

* Name: **ekman**
* Operating System: = 3.10.0-1160.el7.x86_64 GNU/Linux 
* Scheduler: **SLURM 19.05.3**
* Nodes:

  * **1 x Login Node** (:code:`sail.msk.ru -p 2240`) configured as:

    * Model: ???
    * CPU: 112 x Intel(R) Xeon(R) E5-2640 @ 2.50GHz ????

      * Each of the 2 CPUs has 6C/12T, but Hyper-Threading is disabled on the login nodes; so each login node has a total of 12C/12T.

    * RAM: 64 GiB
    * Disk: ???

  * **34 x Compute Nodes** configured as:

    * Model: Intel(R) Xeon(R) ?? 
    * CPU: **2 x** Intel(R) Xeon(R) **E5-2680 v2 @ 2.80GHz**

      * Each of the 2 CPUs has 10C/20T. Hyper-Threading is *enabled*, so each node as a total of **20C/40T**.

    * RAM:

      * **184 nodes with 40 GiB** (2 GiB / core)
      * **24 nodes with 160 GiB** (8 GiB / core)
      * **8 nodes with 320 GiB** (16 GiB / core)
      * **8 nodes with 64 GiB** (3.2GiB / core, **GPU nodes only**)

    * GPU:

      * **1 nodes**, each with **2 sockets x 44 cores pet soket** in total **176 NVIDIA Tesla ???** (each card has ??? GB GDDR5 memory).

    * Disk: ???

 

* Storage:

  * Filesystem: Lustre ???
  * :code:`/home`:

    * Total: ?? TiB (2 x OST with ?? TiB each)

    * User quota: **?? GiB (hard limit: ?? GiB)**

  * :code:`/scratch`:

    * Total: ?? TiB (2 x OST with ?? TiB each)

    * User quota: **?? GiB (hard limit: ?? GiB)**



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
  | gpu         |    ?    | ?            | ???????         |       ??      |            |
  +-------------+---------+--------------+-----------------+---------------+------------+


.. note:: **Clarification on max memory:** on the the broadwellr2, r2c2 and rack1 queues you can normally ask for ??? MB max memory. However, there are also additional nodes with bigger memory. As as you can see in the :ref:`Specs Sheet<Specs Sheet>`, though, there are not enough "big memory" nodes for all the possible configurations, as there are only ?? nodes with ?? MB max memory and only ?? nodes with ?? MB max memory. This means you have to be careful with big memory nodes if you queue jobs in ?? or ??. For example, it makes little sense to queue a job requiring all the ?? nodes with ?? MB max memory in the wide queue, which in principle is useful only for a number of nodes greater than ??. Since there are only ?? nodes with ?? MB max memory, it would make more sense to take advantage of the increased max time in the ? queue and queue it there.


.. note:: **Clarification on threads:** since Hyper-Threading is enabled on all nodes, there are 2 threads per physical core. However, in SLURM's job script language, every thread is a CPU; this means that if you ask for "40 CPUs" in regular1 you are actually asking 40 threads, which is 20 physical cores. For a clarification on the definition on socket, core and thread take a look at the picture below.


.. figure:: res/???.png
   :width: 67%
   :alt: ekman
   :align: center
   
   Definitions of Socket, Core, & Thread. From `SLURM's documentation <https://slurm.schedmd.com/mc_support.html>`_.


